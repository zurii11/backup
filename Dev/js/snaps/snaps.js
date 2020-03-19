let firstName = "ზურა";
let lastName = "ალექსაია";
let snaps; // true or false

let names = [firstName, lastName];
let vowels = ['ა', 'ე', 'ი', 'ო', 'უ']; // Georgian vowels
let consonants = ['ბ', 'გ', 'დ', 'ვ', 'ზ', 'თ', 'კ', 'ლ', 'მ', 'ნ', 'პ', 'ჟ', 'რ', 'ს', 'ტ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']; // Georgian consonants
let vowInF = []; // indexes of vowels in firstName
let conInF = []; // indexes of consonants in firstName
let vowInL = []; // indexes of vowels in lastName
let conInL = []; // indexes of consonants in lastName
let explainedVF = []; // corrected indexes of vowels in firstName
let explainedCF = []; // corrected indexes of consonants in firstName
let explainedVL = []; // corrected indexes of vowels in lastName
let explainedCL = []; // corrected indexes of consonants in lastNames

function setup() {
    canvas = createCanvas(500, 500);
    dismantle();
    explain();
}

function draw() {
    background(20);
}

function snapsIsOrNot() {
    if (names[0] === firstName) {
        snaps = true;
    } else {
        snaps = false;
    }
}

function dismantle() {
    for (let i = 0; i < names.length; i++) {
        let nameChars = names[i].split('');
        let testV = [];
        let testC = [];

        if (names[i] === firstName) {
            vowInF = testV;
            conInF = testC;
        } else {
            conInL = testC;
            vowInL = testV;
        }
        //console.log(testV);
        //console.log(testC);
        //console.log(nameChars);

        for (let i = 0; i < nameChars.length; i++) {
            if (vowels.indexOf(nameChars[i]) === -1) {
                let no = consonants.indexOf(nameChars[i]);
                testC.push(no);
            } else {
                let no = vowels.indexOf(nameChars[i]);
                testV.push(no);
            }
        }
    }
}

function explain() {
    for (let i = 0; i < vowInF.length; i++) {
        explainedVF.push(vowInF[i] + 1);
    }
    
    for (let i = 0; i < conInF.length; i++) {
        explainedCF.push(conInF[i] + 1);
    }

    for (let i = 0; i < vowInL.length; i++) {
        explainedVL.push(vowInL[i] + 1);
    }
    
    for (let i = 0; i < conInL.length; i++) {
        explainedCL.push(conInL[i] + 1);
    }

    console.log(explainedVF);
    console.log(explainedCF);
    console.log(explainedVL);
    console.log(explainedCL);
}