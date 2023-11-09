<script setup lang="ts">

import {ref} from "vue";

import StockChart from '@/components/stocks/StockChart.vue';
import type {Stock} from '@/types/stock';
import {stocksSocket} from "@/services/gatewayController";
import type {StockImprintWithDate} from "@/types/stockImprint";

const payload = defineProps<{ stock: Stock }>();

const dateRef = ref('2021-01-01');

stocksSocket.on('updateStock', async (stock: StockImprintWithDate) => {
  updateDate(stock.date);
});

function updateDate(date: string) {
  dateRef.value = date;
}

</script>

<template>

  <stock-chart :stock="payload.stock" :date="dateRef"/>

</template>

<style scoped>

</style>