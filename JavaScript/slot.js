

const prompt = require('prompt-sync')();

const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = {
    A : 2,
    B : 4,
    C : 5,
    D : 9,
}

const SYMBOL_VALUES = {
    A : 4,
    B : 3,
    C : 2,
    D : 1
}


const deposit = () => {
    while (true){
        const depositAmount = prompt("Enter a Deposit Amount: ");
        const numberOfAmount = parseFloat(depositAmount);

        if (isNaN(numberOfAmount) || numberOfAmount <= 0){
            console.log("Invalid amount of Deposit, please Try Again");
        } else{
            return numberOfAmount;
        }
    }
};

const getNumberOfLines = () => {
    while (true){
        const numberOfLines = prompt("Enter the number of Lines you want to Bet: ");
        const linesAmount = parseFloat(numberOfLines);
        if (isNaN(linesAmount) || linesAmount <= 0 || linesAmount > 3){
            console.log("Invalid number of lines, Please Try Again");
        } else{
            return linesAmount;
        }
    }
};


const getBet = (balance, lines) => {
    while (true){
        const betAmount = prompt("Enter your Betting amount: ");
        const realBetAmount = parseFloat(betAmount);
        if(isNaN(realBetAmount) || realBetAmount <= 0 || realBetAmount > (balance / lines)){
            console.log("Your balance is not enough for this Bet");
        }else {
            return realBetAmount;
        }
    }
};

const spin = () => {
    const symbols = [];
    for (const[symbol, count] of Object.entries(SYMBOLS_COUNT)){
        for(let i = 0; i < count; i++){
            symbols.push(symbol);
        }
    }
    const reels = [];
    for(let i = 0; i < COLS ; i++){
        reels.push([]);
        const reelSymbols = [...symbols];
        for(let q = 0; q < ROWS ; q++){
            const randomIndex = Math.floor(Math.random() * reelSymbols.length);
            const selectedSymbol = reelSymbols[randomIndex];
            reels[i].push(selectedSymbol);
            reelSymbols.splice(randomIndex, 1);
        }
    }
    return reels;
};

const transpose = (reels) => {
    const rows = [];

    for (let i = 0 ; i < ROWS; i++){
        rows.push([]);
        for (let q = 0; q < COLS; q++){
            rows[i].push(reels[q][i])
        }
    }

    return rows;
};

const printRows = (rows) => {
    for(const row of rows){
        let rowString = "";
        for (const [i , symbol] of row.entries()){
            rowString += symbol;
            if (i != row.length - 1){
                rowString += "|"
            }
        }
        console.log(rowString);
    }
};

const getWins = (rows, bet, lines) => {
    let winnings = 0;

    for(let row = 0 ; row < lines ; row++){
        const symbols = rows[row];
        let allSame = true;

        for(const symbol of symbols){
            if(symbol != symbols[0]){
                allSame = false;
                break;
            }
        }
        if (allSame){
            winnings += bet * SYMBOL_VALUES[symbols[0]];}
    }

    return winnings;
};

const game = () => {
    let balance = deposit();
    while (true){
        console.log("You have a balance $" + balance);
        const numberOfLines = getNumberOfLines();
        const realBetAmount = getBet(balance,numberOfLines);
        balance -= realBetAmount * numberOfLines; 
        const reels = spin();
        const rows = transpose(reels);
        printRows(rows);
        const winnings = getWins(rows, realBetAmount, numberOfLines);
        balance += winnings;
        console.log("You won , $" + winnings.toString());
        if(balance <= 0){
            console.log("You run out of money");
            break;
        }
        const playAgain = prompt("Do you want to play again (y/n)? ");
        if (playAgain != "y") break;
    }
}


game();