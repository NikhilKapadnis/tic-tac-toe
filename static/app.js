let board = ["","","","","","","","",""];
let gameOver = false;

const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const resetBtn = document.getElementById("reset");

function render() {
  boardEl.innerHTML = "";
  board.forEach((v,i) => {
    const cell = document.createElement("div");
    cell.className = "cell";
    cell.textContent = v;
    cell.onclick = () => clickCell(i);
    boardEl.appendChild(cell);
  });
}

async function clickCell(i) {
  if (board[i] || gameOver) return;

  board[i] = "X";
  render();

  const res = await fetch("/move", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({ board })
  });

  const data = await res.json();
  board = data.board;
  render();

  if (data.result) {
    gameOver = true;

    if (data.result === "X") {
      statusEl.textContent = "🎉 You win!";
    } else if (data.result === "O") {
      statusEl.textContent = "🤖 Computer won";
    } else {
      statusEl.textContent = "😐 Draw";
    }
  }
}

resetBtn.onclick = () => {
  board = ["","","","","","","","",""];
  gameOver = false;
  statusEl.textContent = "Your turn";
  render();
};

render();
