<script setup>
import { usePageStore } from '@/stores/pages.js'
import EpitaphPage from './components/EpitaphPage.vue'
import FinalPage from './components/FinalPage.vue'
import MainPage from './components/MainPage.vue'
import ProgressBar from './components/ProgressBar.vue'
const page = usePageStore()
</script>

<template>
	<div class="wrapper">
		<MainPage v-show="page.currentPage == page.main" />
		<EpitaphPage v-show="page.currentPage == page.questions" />
		<FinalPage v-show="page.currentPage == page.final" />
	</div>
	<ProgressBar class="progress" />
</template>
<style scoped>
template {
	position: relative;

	& .wrapper {
		max-height: 98%;
	}
	& .progress {
	}
}
</style>
