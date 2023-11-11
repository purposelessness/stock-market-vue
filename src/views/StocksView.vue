<script setup lang="ts">

import StockCard from '@/components/stocks/StockCard.vue';
import type {Stock} from '@/types/stock';
import {getStocks} from '@/services/httpController';
import {onMounted, ref, watch} from "vue";
import {stocksSocket} from "@/services/gatewayController";

const stocks = ref([] as Stock[]);
const selectedStockName = ref(undefined);
const selectedStock = ref(undefined);

getStocks().then((stocksResponse: Stock[]) => {
  stocks.value = stocksResponse;
  if (stocks.value.length > 0) {
    selectedStockName.value = stocks.value[0].name;
  }
});

watch(selectedStockName, () => {
  selectedStock.value = getStockByName(selectedStockName.value);
});

function getStockByName(name: string): Stock | undefined {
  return stocks.value.find((stock: Stock) => stock.name === name);
}

onMounted(() => {
  stocksSocket.emit('findAll');
});

</script>

<template>

  <p v-if="stocks.length === 0">No stocks to display</p>
  <div v-else>
    <select v-model="selectedStockName">
      <option v-for="stock in stocks" :key="stock.id" :value="stock.name">{{ stock.name }}</option>
    </select>
    <stock-card v-if="selectedStock != null" :stock="selectedStock"/>
  </div>

</template>

<style scoped>

</style>