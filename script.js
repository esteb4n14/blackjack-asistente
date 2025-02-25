// Estrategia de Blackjack
const estrategia = {
    duros: {
        4:  {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        5:  {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        6:  {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        7:  {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        8:  {'2': 'P', '3': 'P', '4': 'P', '5': 'P', '6': 'P', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        9:  {'2': 'P', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        10: {'2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D', '10': 'P', 'A': 'P'},
        11: {'2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D', '10': 'D', 'A': 'D'},
        12: {'2': 'P', '3': 'P', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        13: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        14: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        15: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'P', '10': 'R', 'A': 'P'},
        16: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'P', '8': 'P', '9': 'R', '10': 'R', 'A': 'R'},
        17: {'2': 'Q', '3': 'Q', '4': 'Q', '5': 'Q', '6': 'Q', '7': 'Q', '8': 'Q', '9': 'Q', '10': 'Q', 'A': 'Q'}
    },
    blandos: {
        'A,2': {'2': 'P', '3': 'P', '4': 'P', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        'A,3': {'2': 'P', '3': 'P', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        'A,4': {'2': 'P', '3': 'P', '4': 'D', '5': 'D', '6': 'D', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'}
    },
    pares: {
        '2,2': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'S', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '3,3': {'2': 'S', '3': 'S', '4': 'S', '5': 'S', '6': 'S', '7': 'S', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '4,4': {'2': 'P', '3': 'P', '4': 'P', '5': 'S', '6': 'S', '7': 'P', '8': 'P', '9': 'P', '10': 'P', 'A': 'P'},
        '5,5': {'2': 'D', '3': 'D', '4': 'D', '5': 'D', '6': 'D', '7': 'D', '8': 'D', '9': 'D', '10': 'P', 'A': 'P'}
    }
};

// Variables globales
let playerSelectedCards = [];
let dealerSelectedCard = null;

// Función para crear botones de cartas
function createCardButtons(containerId, start, end, callback) {
    const container = document.getElementById(containerId);
    for (let i = start; i <= end; i++) {
        const btn = document.createElement('button');
        btn.className = 'card-btn';
        btn.textContent = i;
        btn.onclick = () => callback(i);
        container.appendChild(btn);
    }
    const aceBtn = document.createElement('button');
    aceBtn.className = 'card-btn';
    aceBtn.textContent = 'A';
    aceBtn.onclick = () => callback(1);
    container.appendChild(aceBtn);
}

// Funciones para determinar el tipo de mano
function determinarTipoMano(mano) {
    if (mano.length === 2 && mano[0] === mano[1]) return 'pares';
    if (mano.includes(1)) {
        const total = mano.reduce((a, b) => a + b, 0);
        return total + 10 <= 21 ? 'blandos' : 'duros';
    }
    return 'duros';
}

// Obtener la acción recomendada
function obtenerAccion(jugador, crupier) {
    const tipoMano = determinarTipoMano(jugador);
    if (tipoMano === 'duros') {
        const total = jugador.reduce((a, b) => a + b, 0);
        return estrategia.duros[total]?.[crupier.toString()] || 'P';
    } else if (tipoMano === 'blandos') {
        const valorBlando = `A,${jugador.find(c => c !== 1)}`;
        return estrategia.blandos[valorBlando]?.[crupier.toString()] || 'P';
    } else {
        return estrategia.pares[jugador.join(',')]?.[crupier.toString()] || 'P';
    }
}

// Manejadores de eventos
function handlePlayerCardSelection(card) {
    if (playerSelectedCards.length < 2) {
        playerSelectedCards.push(card);
        updateSelectedCards();
    }
}

function handleDealerCardSelection(card) {
    dealerSelectedCard = card;
    updateSelectedCards();
}

function updateSelectedCards() {
    document.getElementById('selectedPlayerCards').textContent = `Cartas seleccionadas: ${playerSelectedCards.join(', ')}`;
    document.getElementById('selectedDealerCard').textContent = `Carta seleccionada: ${dealerSelectedCard || ''}`;
}

function clearPlayerCards() {
    playerSelectedCards = [];
    updateSelectedCards();
}

function clearDealerCard() {
    dealerSelectedCard = null;
    updateSelectedCards();
}

// Mostrar recomendación
function showRecommendation() {
    if (playerSelectedCards.length !== 2 || !dealerSelectedCard) {
        document.getElementById('result').textContent = 'Selecciona las cartas primero';
        return;
    }
    const accion = obtenerAccion(playerSelectedCards, dealerSelectedCard);
    const acciones = { 'P': 'Pedir', 'Q': 'Quedarse', 'D': 'Doblar', 'S': 'Separar', 'R': 'Rendirse' };
    document.getElementById('result').textContent = `Recomendación: ${acciones[accion] || 'Acción desconocida'}`;
}

// Inicialización
window.onload = function() {
    createCardButtons('playerCards', 2, 10, handlePlayerCardSelection);
    createCardButtons('dealerCards', 2, 10, handleDealerCardSelection);
    document.getElementById('clearPlayerCards').onclick = clearPlayerCards;
    document.getElementById('clearDealerCard').onclick = clearDealerCard;
    document.getElementById('getStrategy').onclick = showRecommendation;
};