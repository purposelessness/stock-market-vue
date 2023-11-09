<script setup lang="ts">

import StockCard from '@/components/stocks/StockCard.vue';
import type {Stock} from '@/types/stock';
import {getStocks} from '@/services/httpController';
import {onMounted, ref} from "vue";

const stocks = ref([] as Stock[]);

getStocks().then((stocksResponse: Stock[]) => {
  stocks.value = stocksResponse;
});

</script>

<template>

  <p v-if="stocks.length === 0">No stocks to display</p>
  <div v-else>
    <stock-card :stock="stocks.at(0) as Stock"/>
    <!--    <stock-card v-for="stock in stocks" :key="stock.symbol" :stock="stock"/>-->
  </div>

</template>

<style scoped>

</style>