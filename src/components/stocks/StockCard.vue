<script setup lang="ts">

import {ref, watch} from "vue";

import StockChart from '@/components/stocks/StockChart.vue';
import type {Stock} from '@/types/stock';
import {stocksSocket} from "@/services/gatewayController";
import type {StockImprint, StockImprintWithDate} from "@/types/stockImprint";
import StockSummary from "@/components/stocks/StockSummary.vue";

const payload = defineProps<{ stock: Stock }>();

const dateRef = ref('2021-01-01');
const stockImprintRef = ref({
  id: payload.stock.id,
  name: payload.stock.id,
  enabled: payload.stock.enabled,
} as StockImprint)

watch(() => payload.stock, () => {
  stockImprintRef.value = {
    id: payload.stock.id,
    name: payload.stock.id,
    enabled: payload.stock.enabled,
  } as StockImprint;
});

stocksSocket.on('updateStock', async (response: StockImprintWithDate) => {
  if (response.stockImprint) {
    if (response.stockImprint.id === payload.stock.id) {
      dateRef.value = response.date;
      stockImprintRef.value = response.stockImprint;
    }
  }
});

</script>

<template>

  <stock-chart :stock="payload.stock" :date="dateRef"/>
  <stock-summary :stock-imprint="stockImprintRef"/>

</template>

<style scoped>

</style>