<script setup lang="ts">

import {ref} from "vue";

import StockChart from '@/components/stocks/StockChart.vue';
import type {Stock} from '@/types/stock';
import {stocksSocket} from "@/services/gatewayController";
import type {StockImprint, StockImprintWithDate} from "@/types/stockImprint";
import StockSummary from "@/components/stocks/StockSummary.vue";

const payload = defineProps<{ stock: Stock }>();

const dateRef = ref('2021-01-01');
const stockImprintRef = ref({} as StockImprint)

stocksSocket.on('updateStock', async (response: StockImprintWithDate) => {
  if (response.stockImprint)
    if (response.stockImprint.id === payload.stock.id) {
      dateRef.value = response.date;
      stockImprintRef.value = response.stockImprint;
    }
});

</script>

<template>

  <div class="stock-wrapper">
    <stock-chart :stock="payload.stock" :date="dateRef"/>
    <stock-summary :stock-imprint="stockImprintRef"/>
  </div>

</template>

<style scoped>

.stock-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

</style>