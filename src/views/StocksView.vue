<script setup lang="ts">

import {onMounted, ref, watch} from "vue";

import StockCard from '@/components/stocks/StockCard.vue';
import type {Stock} from '@/types/stock';
import {getStocks} from '@/services/httpController';
import {brokersSocket, stocksSocket} from "@/services/gatewayController";

const payload = defineProps({
  enabledBuy: {
    type: Boolean,
    default: false,
  },
  brokerId: {
    type: Number,
    default: undefined,
  },
});

const stocks = ref([] as Stock[]);
const selectedStockName = ref(undefined);
const selectedStock = ref(null as Stock | null);

getStocks().then((stocksResponse: Stock[]) => {
  stocks.value = stocksResponse;
  if (stocks.value.length > 0) {
    selectedStockName.value = stocks.value[0].name;
  }
});

watch(selectedStockName, () => {
  selectedStock.value = getStockByName(selectedStockName.value);
  fill(5);
});

function getStockByName(name: string): Stock | undefined {
  return stocks.value.find((stock: Stock) => stock.name === name);
}

onMounted(() => {
  fill(5);
});

function fill(delay: number) {
  setTimeout(() => {
    stocksSocket.emit('findAll');
  }, delay);
}

const quantity = ref(0);

function buy() {
  if (selectedStock.value == null) {
    return;
  }
  if (payload.brokerId == null) {
    return;
  }

  brokersSocket.emit('buy', {
    brokerId: payload.brokerId,
    stockId: selectedStock.value.id,
    quantity: quantity.value,
  });
}

function sell() {
  if (selectedStock.value == null) {
    return;
  }
  if (payload.brokerId == null) {
    return;
  }

  brokersSocket.emit('sell', {
    brokerId: payload.brokerId,
    stockId: selectedStock.value.id,
    quantity: quantity.value,
  });
}

</script>

<template>

  <p v-if="stocks.length === 0">No stocks to display</p>
  <div v-else class="card-wrapper">
    <select v-model="selectedStockName">
      <option v-for="stock in stocks" :key="stock.id" :value="stock.name">{{ stock.name }}</option>
    </select>
    <stock-card v-if="selectedStock != null && selectedStock.enabled" :stock="selectedStock"/>
    <p v-else>Stock not found</p>
    <div v-if="enabledBuy && selectedStock != null && selectedStock.enabled">
      <label for="quantity">Quantity: </label>
      <input id="quantity" type="number" v-model="quantity"/>
      <button id="buyButton" @click="buy">Buy</button>
      <button id="sellButton" @click="sell">Sell</button>
    </div>
  </div>

</template>

<style scoped>

.card-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

</style>