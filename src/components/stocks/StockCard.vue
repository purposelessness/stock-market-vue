<script setup lang="ts">

import StockChart from '@/components/stocks/StockChart.vue';
import type {Stock} from '@/types/stock';
import {onMounted} from "vue";

const payload = defineProps<{ stock: Stock }>();

</script>

<template>

  <stock-chart :stock="payload.stock"/>

</template>

<style scoped>

</style>