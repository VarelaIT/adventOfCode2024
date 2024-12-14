import fs from "fs"

const inputFile = fs.readFileSync("./input.txt", "utf-8")
const lines = inputFile.split('\n');

/*
let count = 0;

function evalX(arr: string[], l: number, i: number){
    let count = 0;
    if(l > 2 && arr[l][i].length - 3){
        let m = arr[l - 1][i + 1];
        let a = arr[l - 2][i + 2];
        let s = arr[l - 3][i + 3];
        if(m === "M" && a === "A" && s === "S")
            count += 1;
    }
    if(i < arr[l].length - 3){
        let m = arr[l][i + 1];
        let a = arr[l][i + 2];
        let s = arr[l][i + 3];
        if(m === "M" && a === "A" && s === "S")
            count += 1;
    }
    if(l < arr.length - 3){
        let m = arr[l + 1][i];
        let a = arr[l + 2][i];
        let s = arr[l + 3][i];
        if(m === "M" && a === "A" && s === "S")
            count += 1;
    }
    if(l < arr.length - 3 && i < arr[l].length - 3){
        let m = arr[l + 1][i + 1];
        let a = arr[l + 2][i + 2];
        let s = arr[l + 3][i + 3];
        if(m === "M" && a === "A" && s === "S")
            count += 1;
    }

    return count;
}


function evalS(arr: string[], l: number, i: number){
    let count = 0;
    if(l > 2 && arr[l][i].length - 3){
        let a = arr[l - 1][i + 1];
        let m = arr[l - 2][i + 2];
        let x = arr[l - 3][i + 3];
        if(a === "A" && m === "M" && x === "X")
            count += 1;
    } 
    if(i < arr[l].length - 3){
        let a = arr[l][i + 1];
        let m = arr[l][i + 2];
        let x = arr[l][i + 3];
        if(a === "A" && m === "M" && x === "X")
            count += 1;
    }
    if(l < arr.length - 3){
        let a = arr[l + 1][i];
        let m = arr[l + 2][i];
        let x = arr[l + 3][i];
        if(a === "A" && m === "M" && x === "X")
            count += 1;
    }
    if(l < arr.length - 3 && i < arr[l].length - 3){
        let a = arr[l + 1][i + 1];
        let m = arr[l + 2][i + 2];
        let x = arr[l + 3][i + 3];
        if(a === "A" && m === "M" && x === "X")
            count += 1;
    }

    return count;
}

for(let l = 0; l < lines.length; l++){
    for(let i = 0; i < lines.length; i++){
        const letter = lines[l][i];
        if(letter === "X"){
            count += evalX(lines, l, i);
        }else if(letter === "S"){
            count += evalS(lines, l, i);
        }
    }
}
*/

let count = 0;

function evalLetter(arr: string[], l: number, i: number){
    let a = arr[l - 1][i - 1];
    let b = arr[l - 1][i + 1];
    let c = arr[l + 1][i - 1];
    let d = arr[l + 1][i + 1];
    if((a === "M" && b === "S" && c === "M" && d === "S") 
        || (a === "S" && b === "M" && c === "S" && d === "M") 
        || (a === "M" && b === "M" && c === "S" && d === "S") 
        || (a === "S" && b === "S" && c === "M" && d === "M")){
        return true;
    }
    console.log("--- ")
    return false;
}

for(let l = 1; l < lines.length - 1; l++){
    for(let i = 1; i < lines.length - 1; i++){
        const letter = lines[l][i];
        if(letter === "A" && evalLetter(lines, l, i)){
            count += 1;
        }
    }
}

console.log("total: ", count)
