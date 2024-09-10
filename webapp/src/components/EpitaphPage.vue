<script setup>
import BackSvg from '@/assets/icons/back-svg.vue'
import StarsSvg from '@/assets/icons/stars-svg.vue'
import { usePageStore } from '@/stores/pages.js'
import { useQuestionStore } from '@/stores/questions.js'
import Swal from 'sweetalert2'
const page = usePageStore()
const dataStore = useQuestionStore()
async function sweetAlert() {
	Swal.fire({
		title: 'Как пользоваться?',
		text: 'Пожалуйста, предоставьте информацию, и мы создадим для вас неповторимую, восхитительно красивую эпитафию, которая станет достойным венцом памяти вашего близкого.',
		color: 'white',
		background: '#4D4163',
		icon: 'info',
		iconColor: '#cb96fe',
		confirmButtonColor: '#cb96fe',
	})
}
</script>

<template>
	<section>
		<div class="title">
			Ответьте на вопросы
			<div @click="sweetAlert" class="logo">?</div>
		</div>

		<div
			class="questions"
			v-for="(value, key) in dataStore.questions"
			:key="key"
		>
			<div class="question">{{ value.question }}</div>

			<div class="fragment">
				<div class="line"></div>
				<textarea v-model="value.answer"></textarea>
			</div>
		</div>

		<footer>
			<div class="btn-with-indicator">
				<div class="indicator">
					<stars-svg />
					{{ page.currentPage }}/{{ page.amountOfPages }}
				</div>
				<div class="buttons">
					<button class="back" @click="page.go_to_previos_page">
						<back-svg />
					</button>

					<button class="next" @click="page.go_to_next_page">Далее</button>
				</div>
			</div>
			<!-- <ProgressBar /> -->
		</footer>
	</section>
</template>

<style scoped>
.title {
	display: flex;
	margin: 0 0 5% 5%;
	font-size: 1.6rem;

	& .logo {
		text-align: center;
		min-width: 40px;
		margin-left: 5%;
		background-color: var(--accent);
		border-radius: 50%;
	}
}

.questions {
	.fragment {
		display: flex;
		margin: 5% 0;
		border-radius: 2px;
		padding-left: 2%;

		& .line {
			min-width: 5px;
			border-radius: 2.5px;
			background-color: var(--accent);
		}

		& textarea {
			margin-left: 8px;
			font-size: 1.1rem;
			background-color: var(--sbg);
			padding: 2% 2% 0;
			outline: none;
			border: none;
			min-width: 95%;
			min-height: 10vh;
			max-width: 95%;
			max-height: 10vh;
			border-radius: 10px;
		}
	}
}

footer {
	margin-top: 10%;
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 10px;

	& .btn-with-indicator {
		width: 95%;
		position: relative;

		& .indicator {
			position: absolute;
			top: -25%;
			right: 8%;
			display: inline-flex;
			border-radius: 10px;
			align-items: center;
			justify-content: center;
			padding: 5px 10px;
			gap: 5px;
			background-color: #ffffff;

			color: var(--accent);
		}

		.buttons {
			min-width: 95%;
			text-align: center;
			max-height: 8vh;
			display: flex;
			gap: 2%;
			& :nth-child(n) {
				min-height: 8vh;
				border-radius: 15px;
				font-size: 1.6rem;
			}

			& .back {
				flex-grow: 1;

				background: var(--sbg);

				& .icon {
					background-image: url('icons/back.png');
					background-repeat: no-repeat;
					background-size: 50px;
					background-position: center center;
				}
			}

			& .next {
				flex-grow: 5;
				background: var(--accent);
			}
		}
	}
}

/* .progresbar {
	display: flex;
	margin-top: 10px;
	margin-left: 5%;

	& .active_pg_bar {
		background: var(--accent);
		height: 5px;
		width: 60%;
	}

	& .passive_pg_bar {
		background: var(--sbg);
		height: 5px;
		width: 35%;
	}
} */
</style>
