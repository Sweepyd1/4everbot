import {ref} from 'vue';
import { defineStore } from 'pinia';


export const useQuestionStore = defineStore('questionStore', {
    state: () => ({
        data: {
            first_name: ref(''),
            family_name: ref(''),
            last_name: ref(''),

            birth_day: ref(''),
            birth_month: ref(''),
            birth_year: ref(''),

            death_day: ref(''),
            death_month: ref(''),
            death_year: ref(''),

            avatar: ref('')
        },
        questions: {
            1: {
                question: 'Какие значимые периоды в его жизни вы бы хотели осветить?',
                answer: ref(''),
            },
            2: {
                question: 'Какие увлечения и хобби у этого человека были?',
                answer: ref('')
            },
            3: {
                question: 'Какие личные качества и достижения вы бы хотели отметить?',
                answer: ref('')
            },
            4: {
                question: 'Какова была жизненная философия этого человека?',
                answer: ref('')
            },
            5: {
                question: 'Есть ли краткое выражение или афоризм, который мог бы отразить его дух?',
                answer: ref('')
            },
            6: {
                question: 'Есть ли какие-то истории или анекдоты, которые вы считаете важными для понимания его личности или жизненного пути?',
                answer: ref('')
            },
            7: {
                question: 'Как этот человек влиял на жизнь других?',
                answer: ref('')
            },
            8: {
                question: 'Какие препятствия или трудности он преодолел в своей жизни?',
                answer: ref('')
            },
            9: {
                question: 'Есть ли особые высказывания или цитаты этого человека, которые вы бы хотели включить?',
                answer: ref('')
            },
            10: {
                question: 'Как бы вы хотели, чтобы его запомнили?',
                answer: ref('')
            },
            11: {
                question: 'Какие слова могли бы утешить или вдохновить тех, кто будет посещать его последнее место упокоения?',
                answer: ref('')
            }
        },
        yandexAnswers:{
            biography:ref('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'),
            epitaph: ref('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip')
        }
    }),
    getters: {
        fullname() {
            return this.data.family_name + ' ' + this.data.first_name + ' ' + this.data.last_name;
        },
        duration_of_life() {
            let trans4 = (value) => {
                switch (value.length) {
                    case 4: return value
                    case 3: return value + "#"
                    case 2: return value + "##"
                    case 1: return value + "###"
                    case 0: return value + "####"
                    default: return value.slice(4)
                }
            }

            let trans2 = (value) => {
                switch (value.length) {
                    case 2: return value
                    case 1: return value + "#"
                    case 0: return value + "##"
                    default: return value.slice(2)
                }
            }

            return [trans2(this.data.birth_day), trans2(this.data.birth_month), trans4(this.data.birth_year)].join(".")
                + "-" +
                [trans2(this.data.death_day), trans2(this.data.death_month), trans4(this.data.death_year)].join(".")
        }
    }
})
