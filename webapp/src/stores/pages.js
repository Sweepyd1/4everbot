import { defineStore } from 'pinia'
import { ref } from 'vue'

export const usePageStore = defineStore('pageStore', {
	state: () => ({
		main: 1,
		questions: 2,
		final: 3,
		currentPage: ref(1),
		amountOfPages: 3,
		ProgressBarPrecentenge: ref(33.3),
	}),

	actions: {
		go_to_next_page() {
			this.currentPage++
			this.ProgressBarPrecentenge = +this.ProgressBarPrecentenge + 33.3
		},
		go_to_previos_page() {
			this.currentPage--
			this.ProgressBarPrecentenge = +this.ProgressBarPrecentenge - 33.3
		},
	},
	getters: {
		get_ProgressBarPrecentenge() {
			return this.ProgressBarPrecentenge + '%'
		},
	},
})
