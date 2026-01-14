from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random

app = FastAPI()

class Move(BaseModel):
    board: list  # 9 items: "X", "O", ""

WIN_PATTERNS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6),
]

def check_winner(board):
    for a,b,c in WIN_PATTERNS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if "" not in board:
        return "draw"
    return None

def ai_move(board):
    empty = [i for i,v in enumerate(board) if v == ""]
    return random.choice(empty) if empty else None

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/move")
def play(move: Move):
    board = move.board
    if len(board) != 9:
        raise HTTPException(400, "Invalid board")

    result = check_winner(board)
    if result:
        return {"board": board, "result": result}

    ai = ai_move(board)
    if ai is not None:
        board[ai] = "O"

    result = check_winner(board)
    return {"board": board, "result": result}

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
def home():
    return FileResponse(str(STATIC_DIR / "index.html"))
