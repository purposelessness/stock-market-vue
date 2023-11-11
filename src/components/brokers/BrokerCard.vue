<script setup lang="ts">

import type {Broker} from "@/types/broker";

const payload = defineProps<{ broker: Broker, stockPrices: any }>();

function getPrice(id: number): string {
  if (payload.stockPrices[id] === undefined) {
    return '?';
  }
  return payload.stockPrices[id];
}

function getProfit(priceBought: number, quantity: number, id: number): string {
  if (payload.stockPrices[id] === undefined) {
    return '?';
  }
  const profit: number = (payload.stockPrices[id] - priceBought) * quantity;
  return profit > 0 ? `+${profit.toFixed(2)}` : profit.toFixed(2);
}

</script>

<template>

  <div class="broker-card">
    <h1>{{ payload.broker.login }}</h1>
    <h2>Money: {{ payload.broker.money.toFixed(2) }}$</h2>

    <h2>Stocks: <span v-if="payload.broker.actives.length === 0">None</span></h2>
    <div class="broker-stocks">
      <div v-for="actives in payload.broker.actives" :key="`actives-${actives.id}`">
        <div v-for="stock in actives.value" :key="`stock-${stock.id}`">
          <p>{{ stock.name }}: {{ stock.quantity }} x {{ getPrice(stock.id) }} ->
            {{ getProfit(stock.price, stock.quantity, stock.id) }}</p>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>

.broker-card {
  border: 1px solid black;
  padding: 1rem;
  margin: 1rem;
  width: 100%;
  background: hsla(170, 100%, 20%, 0.5);
}

</style>