import fs from "fs"

const inputFile = fs.readFileSync("./input.txt", "utf-8")
const inputLines = inputFile.split('\r\n');
const leftList: number[] = [];
const rightList: number[] = [];
inputLines.forEach((line)=>{
    const pair = line.split(" ");
    leftList.push(parseInt(pair[0]))
    rightList.push(parseInt(pair[3]))
});

function compareNumbers(previous: number, current: number){
        return previous - current;
}

leftList.sort(compareNumbers)
rightList.sort(compareNumbers)

/*
const result = leftList.reduce((value: number, current: number, i: number, all: number[])=> {
    let diff = current - rightList[i];
    if(diff < 0)
        diff *= -1;
    return value + diff;
}, 0);
*/

const result2 = leftList.reduce((value: number, current: number, i: number, all: number[])=> {
    let times = rightList.reduce((times: number, coincidence: number, i: number, all: number[])=> {
        if(current === coincidence)
            times += 1;
        return times
    }, 0);
    let prod = current * times;
    return value + prod;
}, 0);

console.log(result2)