<script setup>
import AddPhotoSvg from '@/assets/icons/add-photo-svg.vue'
import CalendarSvg from '@/assets/icons/calendar-svg.vue'
import StarsSvg from '@/assets/icons/stars-svg.vue'
import { usePageStore } from '@/stores/pages.js'
import { useQuestionStore } from '@/stores/questions.js'
import { ref } from 'vue'
const page = usePageStore()
const dataStore = useQuestionStore()
const dateSelected = ref(true) // true - birtday; false - deathday;
const choice_image = ref(null) // вспомогательная переменная для ссылки на объект DOM

const validateDateSymbols = (e, name) => {
	if (!(e.data in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) {
		dataStore.data[name] = dataStore.data[name].replace(e.data, '')
	}
}
const onFileChange = e => {
	let reader = new FileReader()
	reader.onloadend = function () {
		dataStore.data.avatar = reader.result
	}
	reader.readAsDataURL(e.target.files[0])
}

const triggerFileInputClick = () => {
	choice_image.value.click()
}
</script>

<template>
	<div class="union">
		<div class="header_and_main">
			<header>
				<div class="img" @click="triggerFileInputClick">
					<input
						type="file"
						accept="image/*"
						@change="onFileChange"
						ref="choice_image"
					/>
					<add-photo-svg class="icon" v-if="!dataStore.data.avatar" />
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
				<div class="fragment">
					<div class="title">Заполните данные</div>

					<article>
						<div class="line"></div>
						<div class="fio-questions">
							<input
								placeholder="Фамилия"
								autocomplete="on"
								v-model="dataStore.data.family_name"
							/>
							<input
								placeholder="Имя"
								autocomplete="on"
								v-model="dataStore.data.first_name"
							/>
							<input
								placeholder="Отчество"
								autocomplete="on"
								v-model="dataStore.data.last_name"
							/>
						</div>
					</article>
				</div>

				<div class="dates">
					<button
						v-bind:class="{ buttonInFocus: dateSelected }"
						@click="dateSelected = !dateSelected"
					>
						Дата рождения
					</button>
					<button
						v-bind:class="{ buttonInFocus: !dateSelected }"
						@click="dateSelected = !dateSelected"
					>
						Дата смерти
					</button>
				</div>
				<div class="choice-date">
					<div class="date-birth" v-show="dateSelected">
						<div class="day">
							<input
								maxlength="2"
								v-model="dataStore.data.birth_day"
								@input="validateDateSymbols($event, 'birth_day')"
								placeholder="00"
							/>
							<div class="mini">День</div>
						</div>
						<div class="month">
							<input
								maxlength="2"
								v-model="dataStore.data.birth_month"
								@input="validateDateSymbols($event, 'birth_month')"
								placeholder="00"
							/>
							<div class="mini">Месяц</div>
						</div>
						<div class="year">
							<input
								maxlength="4"
								v-model="dataStore.data.birth_year"
								@input="validateDateSymbols($event, 'birth_year')"
								placeholder="0000"
							/>
							<div class="mini">Год</div>
						</div>
					</div>
					<div class="date-dead" v-show="!dateSelected">
						<div class="day">
							<input
								maxlength="2"
								v-model="dataStore.data.death_day"
								@input="validateDateSymbols($event, 'death_day')"
								placeholder="00"
							/>
							<div class="mini">День</div>
						</div>
						<div class="month">
							<input
								maxlength="2"
								v-model="dataStore.data.death_month"
								@input="validateDateSymbols($event, 'death_month')"
								placeholder="00"
							/>
							<div class="mini">Месяц</div>
						</div>
						<div class="year">
							<input
								maxlength="4"
								v-model="dataStore.data.death_year"
								@input="validateDateSymbols($event, 'death_year')"
								placeholder="0000"
							/>
							<div class="mini">Год</div>
						</div>
					</div>
				</div>
			</main>
		</div>
		<footer>
			<div class="btn-with-indicator">
				<div class="indicator">
					<stars-svg />
					{{ page.currentPage }}/{{ page.amountOfPages }}
				</div>
				<button @click="page.go_to_next_page()">Далее</button>
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
	min-height: 14vh;
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

		& input {
			display: none;
		}

		& img {
			width: 100%;
			height: 100%;
		}

		& .icon {
			width: 40px;
			height: 40px;
		}
	}

	& .text {
		margin-top: 3%;
		min-width: 66%;

		& .FIO {
			font-size: 1.375rem;
			line-height: 27px;

			min-height: 6.5vh;
		}

		& .preview-date {
			display: inline-flex;
			padding: 5px;
			background: var(--accent);
			border-radius: 5px;
			align-items: center;
			gap: 5px;
			margin: 2% 0;

			& .icon {
				width: 20px;
				height: 20px;
			}
		}
	}
}

.buttonInFocus {
	background: var(--accent) !important;
	transition: all 0.3s ease;
}

main {
	& .fragment {
		display: flex;
		flex-direction: column;
		gap: 15px;

		& .title {
			padding-left: 2%;
			font-size: 1.6rem;
			margin-top: 5%;
		}

		& article {
			display: flex;
			width: 100%;

			& .line {
				width: 5px;
				border-radius: 2.5px;
				background-color: var(--accent);
			}

			& .fio-questions {
				display: flex;
				flex-direction: column;
				gap: 10px;
				width: 100%;
				padding-left: 10px;

				& input {
					height: 65px;
					font-size: 18px;
					background-color: var(--sbg);
					padding: 0 10px;
					outline: none;
					border: none;
					width: 100%;
					border-radius: 10px;
				}
			}
		}
	}

	& .dates {
		margin-top: 20px;
		background: var(--sbg);
		padding: 1%;
		border-radius: 10px;

		& button {
			font-size: 1.2rem;
			background-color: var(--sbg);
			min-width: 49%;
			min-height: 3rem;
			border-radius: 10px;
			transition: all 0.3s ease;

			&:nth-child(1) {
				margin-right: 2%;
			}
		}
	}

	& .choice-date {
		margin-top: 10px;

		& :nth-child(n) {
			display: flex;
			gap: 10px;
			align-content: center;
		}

		& .day,
		.month {
			position: relative;
			width: 25%;
		}

		& .year {
			position: relative;
			width: 52%;
			& .mini {
				width: 30%;
			}
		}

		& input {
			width: 100%;
			height: 8vh;
			background: var(--sbg);
			outline: none;
			border: none;
			border-radius: 15px;
			text-align: center;
			font-size: 2.5rem;
		}

		& .mini {
			height: 1.6vh;
			width: 50%;
			position: absolute;
			bottom: -0.8vh;
			left: 50%;
			transform: translateX(-50%);
			background-color: var(--accent);

			justify-content: center;
			border-radius: 5px;
			font-size: 0.5625rem;
		}
	}
}

footer {
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 10px;
	top: auto;
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
			font-weight: normal;
			color: var(--accent);
		}

		& button {
			height: 70px;
			background: var(--accent);
			width: 100%;
			border-radius: 20px;
			font-size: 1.6rem;
		}
	}
}
</style>
