<script setup>
import BackSvg from '@/assets/icons/back-svg.vue'
import CalendarSvg from '@/assets/icons/calendar-svg.vue'
import PersonSvg from '@/assets/icons/person-svg.vue'
import StarsSvg from '@/assets/icons/stars-svg.vue'
import { usePageStore } from '@/stores/pages.js'
import { useQuestionStore } from '@/stores/questions.js'
import Swal from 'sweetalert2'
const page = usePageStore()
const dataStore = useQuestionStore()

async function sweetAlert() {
	Swal.fire({
		title: 'Как пользоваться?',
		text: "Здесь вы можете видеть сгенерированные биографию и эпитафию, вы спокойно можете их редактировать и, если они вам не нравятся, полностью менять, нажимая кнопку 'Перегенерировать'",
		color: 'white',
		background: '#4D4163',
		icon: 'info',
		iconColor: '#cb96fe',
		confirmButtonColor: '#cb96fe',
	})
}
</script>

<template>
	<div class="union">
		<div>
			<header class="header_and_main">
				<div class="img" @click="triggerFileInputClick">
					<PersonSvg class="icon" v-if="!dataStore.data.avatar" />
					<img class="avatar" :src="dataStore.data.avatar" alt="" v-else />
				</div>
				<div class="text">
					<div class="FIO" v-if="dataStore.fullname !== '  '">
						{{ dataStore.fullname }}
					</div>
					<div class="FIO" style="color: #6d7172" v-else>
						Фамилия Имя Отчество
					</div>
					<div class="preview-date">
						<calendar-svg class="icon" />
						<div class="value">{{ dataStore.duration_of_life }}</div>
					</div>
				</div>
			</header>
			<main>
				<div class="title">Биография <button>cгенерировать</button></div>
				<div class="fragment">
					<div class="line"></div>
					<textarea
						v-model="dataStore.yandexAnswers.biography"
						class="biography"
					></textarea>
				</div>
				<div class="title">Эпитафия <button>cгенерировать</button></div>
				<div class="fragment">
					<div class="line"></div>
					<textarea
						v-model="dataStore.yandexAnswers.epitaph"
						class="epitaph"
					></textarea>
				</div>
			</main>
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

					<button class="next">Опубликовать</button>
				</div>
			</div>
			<!-- <ProgressBar /> -->
		</footer>
	</div>
</template>

<style scoped>
.union {
	min-height: 96vh;
	max-height: 96vh;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}
header {
	display: flex;
	min-width: 100%;
	max-width: 100%;
	height: 14vh;
	align-items: center;
	gap: 20px;
	padding: 0 20px;
	background-color: var(--sbg);
	border-radius: 15px;

	& .img {
		max-width: 100px;
		max-height: 100px;
		min-width: 100px;
		min-height: 100px;
		background-color: var(--light-sbg);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;

		& img {
			width: 100%;
			height: 100%;
		}

		& .icon {
			width: 70%;
			height: 70%;
		}
	}

	& .text {
		margin-top: 3%;
		min-width: 66%;

		& .FIO {
			font-size: 1.375rem;
			line-height: 27px;
			margin-bottom: 3%;
			min-height: 6.5vh;
		}

		& .preview-date {
			display: inline-flex;
			padding: 5px;
			background: var(--accent);
			border-radius: 5px;
			align-items: center;
			gap: 5px;
			margin: 2% 0 5%;
			& .icon {
				width: 20px;
				height: 20px;
			}
		}
	}
}

main {
	& .title {
		padding-left: 2%;
		font-size: 1.6rem;
		margin-top: 5%;
		display: flex;
		direction: row;
		justify-content: left;
		align-items: baseline;
		gap: 15px;
		& .logo {
			text-align: center;
			font-size: 1.3rem;
			min-width: 1.5625em;
			max-width: 1.5625em;
			background-color: var(--accent);
			border-radius: 50%;
		}
	}

	& button {
		height: 1.7rem;
		background: var(--accent);
		border-radius: 5px;
		font-size: 1.2rem;
	}

	& .fragment {
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
			outline: none;
			border: none;
			padding: 2% 2% 0;
			min-width: calc(100% - 13px);
			min-height: 20vh;
			max-width: calc(100% - 13px);
			max-height: 30vh;
			border-radius: 10px;
		}

		& .biography {
			min-height: 25vh;
		}
	}
}

footer {
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

			& :nth-child(n) {
				min-height: 8vh;
				border-radius: 15px;
				font-size: 1.6rem;
			}

			& .back {
				flex-grow: 1;
				margin-right: 2%;
				background: var(--sbg);

				& .icon {
					background-image: url('icons/back.png');
					background-repeat: no-repeat;
					background-size: 50px;
					background-position: center center;
				}
			}

			& .next {
				flex-grow: 3;
				background: var(--accent);
			}
		}
	}
}
</style>
