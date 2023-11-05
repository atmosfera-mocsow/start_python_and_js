console.log("Hello, Work!")
// TODO: написать много нового кода
//  переменные
var school = "ШВА"
let school2 = "ШВА"
const school3 = "ШВА"
school2 = "dsadas"
// school3 = "dasdas"

// нейминг переменных
// schoolName - переменные
// SCHOOL_NAME - константы

/*school2 = "dsadas" // сбоку
выфв
*/


// # типы данных
var school_number = 1
var school_float = -2.3
var school_string = "dsadas"
school = "d"
var school_bool = true
var school_list = ["dsa", 312]
school[1]
var school_dict = {"dsa": "dsad", "dsadasd": 231}
school["dsadasd"]

// циклы
// while (true) {
//     console.log("Привет!")
// }

for (let i = 0; i < 3; i++) { // выведет 0, затем 1, затем 2
    console.log("Привет!", i)
}

let school_atmo = [
    "шва19", "шва20", "шва21", 
    "шва22", "шва23",
    "шва24"
]
school_atmo.forEach(school => {console.log(school)})
let years = school_atmo.map(school => school.slice(3,5))
console.log(years)

let years_s = school_atmo.filter(school => parseInt(school.slice(3,5)) >= 20)
console.log(years_s)


// # условия 
if (true) {
    console.log("Hi!")
}
var new_var = school_atmo.includes("шва19") ? "Yes" : "No"

// # булен операторы
let var2 = undefined
var new_var2 = var2 || "No"
// || && !


// const my_fun = (text1, text: number = 1): string => {
//     console.log(text1, text)
//     return "dsadasda"
// }

const my_fun = (text1, text = 1) => {
    console.log(text1, text)
    return "dsadasda"
}

let val = my_fun("text1")
