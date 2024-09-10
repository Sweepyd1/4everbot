<script setup>
import { usePageStore } from '@/stores/pages.js'
const page = usePageStore()
</script>

<template>
	<div class="progressbar">
		<div
			class="active_pg_bar"
			:style="{ '--ProgressBarPrecentenge': page.get_ProgressBarPrecentenge }"
		></div>
	</div>
</template>

<style>
.progressbar {
	display: flex;
	min-height: 5px;
	background: var(--sbg);
	width: 95%;
	height: 5px;
	justify-content: flex-start;
	border-radius: 2.5px;
	overflow: hidden;
	margin-top: 8px;
	margin-left: auto;
	margin-right: auto;

	bottom: 1%;
	max-height: 2%;
	& .active_pg_bar {
		background: var(--accent);
		height: 5px;
		width: var(--ProgressBarPrecentenge);
		transition: all 2s ease-in-out;
	}
}
</style>
