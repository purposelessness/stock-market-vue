<script setup lang="ts">

import {onMounted, ref} from "vue";

import {brokersSocket, stocksSocket} from "@/services/gatewayController";
import type {Broker} from "@/types/broker";
import BrokerCard from "@/components/brokers/BrockerCard.vue";
import type {StockImprintWithDate} from "@/types/stockImprint";

const brokersRef = ref([] as Broker[]);
const dateRef = ref('????-??-??');
const stockPricesRef = ref({});

brokersSocket.emit('findAll', (brokers: Broker[]) => {
  brokersRef.value = brokers;
});

stocksSocket.on('updateStock', (response: StockImprintWithDate) => {
  stockPricesRef.value[response.stockImprint.id] = response.stockImprint.price;
  dateRef.value = response.date;
  console.log(response)
});

onMounted(() => {
  stocksSocket.emit('findAll');
  console.log('findAll');
});

</script>

<template>

  <div class="date-wrapper">
    <h1>Date: {{ dateRef }}</h1>
  </div>

  <div class="brokers-view">
    <div v-for="broker in brokersRef" :key="`broker-${broker.login}`">
      <broker-card :broker="broker" :stock-prices="stockPricesRef"/>
    </div>
  </div>

</template>

<style scoped>

.date-wrapper {
  text-align: center;
  margin: 1rem;
}

</style>