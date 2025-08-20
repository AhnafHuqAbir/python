// Spider / Web Tic-Tac-Toe with Minimax AI + web-shoot animation
const boardEl = document.getElementById('board');
const statusEl = document.getElementById('status');
const btn2p = document.getElementById('btn-2p');
const btnAi = document.getElementById('btn-ai');
const resetBtn = document.getElementById('reset');
const hintBtn = document.getElementById('hint');

let mode = '';           // '2p' or 'ai'
let current = 'X';       // 'X' => Spider (player), 'O' => Web (opponent/AI)
let cells = [];          // DOM cell elements
let over = false;        // game over flag

// map internal marks to emoji
const EMOJI = { X: '🕷️', O: '🕸️' };

// lines
const LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
];

// UI wiring
btn2p.addEventListener('click', () => start('2p'));
btnAi.addEventListener('click', () => start('ai'));
resetBtn.addEventListener('click', resetGame);
hintBtn.addEventListener('click', showHint);

// start
function start(selectedMode) {
    mode = selectedMode;
    btn2p.style.display = btnAi.style.display = 'none';
    resetBtn.style.display = 'inline-block';
    hintBtn.style.display = 'inline-block';
    createBoard();
    over = false;
    current = 'X';
    updateStatus();
}

function createBoard() {
    boardEl.innerHTML = '';
    cells = [];
    for (let i = 0; i < 9; i++) {
        const c = document.createElement('div');
        c.className = 'cell';
        c.dataset.index = i;
        c.dataset.mark = ''; // internal state: '' / 'X' / 'O'
        c.addEventListener('click', () => onCellClick(c), { once: true });
        boardEl.appendChild(c);
        cells.push(c);
    }
}

// click handler
function onCellClick(cell) {
    if (over || cell.dataset.mark) return;
    place(cell, current);
    if (checkWin(current)) {
        gameOver(current);
        return;
    }
    if (isDraw()) { gameDraw(); return; }

    if (mode === '2p') {
        current = current === 'X' ? 'O' : 'X';
        updateStatus();
    } else { // AI mode
        current = 'O';
        updateStatus();
        setTimeout(aiMove, 250); // small delay before AI
    }
}

// place mark (updates dataset and shows emoji with animation)
function place(cell, player) {
    cell.dataset.mark = player;
    cell.innerHTML = `<span class="mark">${EMOJI[player]}</span>`;
    // remove any hint class if present
    cell.classList.remove('hint');
}

// check win by internal mark
function checkWin(player) {
    return LINES.some(([a, b, c]) => cells[a].dataset.mark === player && cells[b].dataset.mark === player && cells[c].dataset.mark === player);
}

function isDraw() {
    return cells.every(c => c.dataset.mark);
}

function gameOver(winner) {
    over = true;
    updateStatus(`${EMOJI[winner]} wins!`);
    // stylish highlight: add victory class to winning cells and subtle to others
    LINES.forEach(line => {
        const [a, b, c] = line;
        if (cells[a].dataset.mark === winner && cells[b].dataset.mark === winner && cells[c].dataset.mark === winner) {
            cells[a].classList.add('victory');
            cells[b].classList.add('victory');
            cells[c].classList.add('victory');
        }
    });
    // if AI wins and mode === 'ai' and winner==='O' => loss visual (shake)
    if (mode === 'ai' && winner === 'O') {
        cells.forEach(c => c.classList.add('loss'));
    }
}

function gameDraw() {
    over = true;
    updateStatus('Draw!');
    cells.forEach(c => c.classList.add('draw'));
}

function updateStatus(text) {
    if (text) { statusEl.textContent = text; return; }
    if (mode === 'ai') {
        statusEl.textContent = (current === 'X') ? 'Your move 🕷️' : 'AI thinking… 🤖';
    } else if (mode === '2p') {
        statusEl.textContent = (current === 'X') ? '🕷️ Spidey turn' : '🕸️ Web turn';
    } else {
        statusEl.textContent = 'Choose a mode to start';
    }
}

// --- AI (Minimax) ---
// AI plays 'O'
function aiMove() {
    if (over) return;
    const best = minimaxDecision();
    if (best != null) {
        const cell = cells[best];
        // simulate click (but avoid re-adding listener)
        place(cell, 'O');
        if (checkWin('O')) { gameOver('O'); return; }
        if (isDraw()) { gameDraw(); return; }
        current = 'X';
        updateStatus();
    }
}

// Minimax decision: returns index of best move
function minimaxDecision() {
    let bestScore = -Infinity;
    let bestMove = null;
    for (let i = 0; i < 9; i++) {
        if (!cells[i].dataset.mark) {
            cells[i].dataset.mark = 'O';
            let score = minimax(0, false);
            cells[i].dataset.mark = '';
            if (score > bestScore) { bestScore = score; bestMove = i; }
        }
    }
    return bestMove;
}

// minimax returns score for current board
function minimax(depth, isMaximizing) {
    if (checkStaticWin('O')) return 10 - depth;
    if (checkStaticWin('X')) return depth - 10;
    if (isStaticDraw()) return 0;

    if (isMaximizing) {
        let best = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (!cells[i].dataset.mark) {
                cells[i].dataset.mark = 'O';
                let val = minimax(depth + 1, false);
                cells[i].dataset.mark = '';
                best = Math.max(best, val);
            }
        }
        return best;
    } else {
        let best = Infinity;
        for (let i = 0; i < 9; i++) {
            if (!cells[i].dataset.mark) {
                cells[i].dataset.mark = 'X';
                let val = minimax(depth + 1, true);
                cells[i].dataset.mark = '';
                best = Math.min(best, val);
            }
        }
        return best;
    }
}

// Helpers used inside minimax that read dataset only (no DOM mutation besides dataset)
function checkStaticWin(player) {
    return LINES.some(([a, b, c]) => cells[a].dataset.mark === player && cells[b].dataset.mark === player && cells[c].dataset.mark === player);
}
function isStaticDraw() {
    return cells.every(c => c.dataset.mark);
}

// --- Hint: show best move for player (X) briefly ---
function showHint() {
    if (over) return;
    // compute best for X (we try each empty cell as X and evaluate)
    let bestScore = -Infinity;
    let bestMove = null;
    for (let i = 0; i < 9; i++) {
        if (!cells[i].dataset.mark) {
            cells[i].dataset.mark = 'X';
            let score = minimax(0, true); // after placing X, it's maximizing for O in our minimax: pass true to pick best O; but to evaluate X we invert logic by taking negative
            cells[i].dataset.mark = '';
            // We want moves that maximize X's position; because minimax returns scores from O's perspective, invert sign:
            let scoreForX = -score;
            if (scoreForX > bestScore) { bestScore = scoreForX; bestMove = i; }
        }
    }
    if (bestMove != null) {
        const c = cells[bestMove];
        c.classList.add('hint');
        setTimeout(() => c.classList.remove('hint'), 1000);
    }
}

// reset
function resetGame() {
    btn2p.style.display = btnAi.style.display = 'inline-block';
    resetBtn.style.display = hintBtn.style.display = 'none';
    boardEl.innerHTML = '';
    mode = '';
    current = 'X';
    cells = [];
    over = false;
    statusEl.textContent = 'Choose a mode to start';
}

// initialize empty board at load
createBoard();
