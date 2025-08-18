const board = document.getElementById('board');
const resetBtn = document.getElementById('reset');
const modeSelect = document.getElementById('mode-select');
const hintBtn = document.getElementById('hintBtn');

let gameMode = '';
let currentPlayer = 'X';
let cells = [];

function startGame(mode) {
    gameMode = mode;
    modeSelect.style.display = 'none';
    resetBtn.style.display = 'inline-block';
    hintBtn.style.display = 'inline-block';
    createBoard();
}

function createBoard() {
    board.innerHTML = '';
    cells = [];
    currentPlayer = 'X';

    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.addEventListener('click', () => handleMove(cell, i), { once: true });
        board.appendChild(cell);
        cells.push(cell);
    }
}

function handleMove(cell, index) {
    if (cell.textContent !== '') return;

    makeMove(cell, currentPlayer);

    if (checkWin(currentPlayer)) {
        highlightAnimation(currentPlayer === 'X' ? 'victory' : 'loss');
        setTimeout(() => alert(`${currentPlayer === 'X' ? 'Spider' : 'Web'} Wins!`), 700);
        return;
    }
    if (isDraw()) {
        highlightAnimation('draw');
        setTimeout(() => alert('Draw! 😐'), 700);
        return;
    }

    if (gameMode === '2p') {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    } else if (gameMode === 'ai') {
        currentPlayer = 'O';
        setTimeout(aiMove, 400);
    }
}

function aiMove() {
    let bestScore = -Infinity;
    let move;

    cells.forEach((cell, i) => {
        if (cell.textContent === '') {
            cell.textContent = 'O';
            let score = minimax(cells, 0, false);
            cell.textContent = '';
            if (score > bestScore) { bestScore = score; move = i; }
        }
    });

    makeMove(cells[move], 'O');

    if (checkWin('O')) {
        highlightAnimation('loss');
        setTimeout(() => alert('AI Wins! 🤖🕸️'), 700);
        return;
    }
    if (isDraw()) {
        highlightAnimation('draw');
        setTimeout(() => alert('Draw! 😐'), 700);
        return;
    }

    currentPlayer = 'X';
}

function makeMove(cell, player) {
    cell.textContent = (player === 'X') ? '🕷️' : '🕸️';
    cell.classList.add("web-anim");
    setTimeout(() => cell.classList.remove("web-anim"), 600);
}

function checkWin(player) {
    const wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
    return wins.some(([a, b, c]) => cells[a].textContent === playerMark(player) && cells[b].textContent === playerMark(player) && cells[c].textContent === playerMark(player));
}

function playerMark(player) { return player === 'X' ? '🕷️' : '🕸️'; }
function isDraw() { return cells.every(cell => cell.textContent); }

function minimax(boardState, depth, isMaximizing) {
    if (checkWin('O')) return 10 - depth;
    if (checkWin('X')) return depth - 10;
    if (isDraw()) return 0;

    if (isMaximizing) {
        let bestScore = -Infinity;
        boardState.forEach((cell, i) => {
            if (cell.textContent === '') {
                cell.textContent = 'O';
                let score = minimax(boardState, depth + 1, false);
                cell.textContent = '';
                bestScore = Math.max(score, bestScore);
            }
        });
        return bestScore;
    } else {
        let bestScore = Infinity;
        boardState.forEach((cell, i) => {
            if (cell.textContent === '') {
                cell.textContent = 'X';
                let score = minimax(boardState, depth + 1, true);
                cell.textContent = '';
                bestScore = Math.min(score, bestScore);
            }
        });
        return bestScore;
    }
}

// Hint button
hintBtn.addEventListener('click', () => {
    const move = getBestHint();
    if (move != null) {
        cells[move].classList.add('hint');
        setTimeout(() => cells[move].classList.remove('hint'), 1000);
    }
});

function getBestHint() {
    let bestScore = -Infinity;
    let move = null;

    cells.forEach((cell, i) => {
        if (cell.textContent === '') {
            cell.textContent = '🕷️';
            let score = minimax(cells, 0, false);
            cell.textContent = '';
            if (score > bestScore) { bestScore = score; move = i; }
        }
    });
    return move;
}

function highlightAnimation(type) {
    cells.forEach(cell => {
        if (type === 'victory') cell.classList.add('victory');
        if (type === 'loss') cell.classList.add('loss');
        if (type === 'draw') cell.classList.add('draw');
    });
}

resetBtn.addEventListener('click', () => { createBoard(); });
