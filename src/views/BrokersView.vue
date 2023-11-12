<script setup lang="ts">

import {onMounted, ref} from "vue";

import {brokersSocket, stocksSocket} from "@/services/gatewayController";
import type {Broker} from "@/types/broker";
import BrokerCard from "@/components/brokers/BrokerCard.vue";
import type {StockImprintWithDate} from "@/types/stockImprint";

const brokersRef = ref([] as Broker[]);
const dateRef = ref('????-??-??');
const stockPricesRef = ref({});

brokersSocket.emit('findAll', (brokers: Broker[]) => {
  brokersRef.value = brokers;
});

brokersSocket.on('updated', (broker: Broker) => {
  const index = brokersRef.value.findIndex((b: Broker) => b.login === broker.login);
  if (index !== -1) {
    brokersRef.value[index] = broker;
  } else {
    brokersRef.value.push(broker);
  }
});

brokersSocket.on('removed', (brokerId: number) => {
  console.log('removed broker', brokerId);
  const index = brokersRef.value.findIndex((b: Broker) => b.id === brokerId);
  if (index !== -1) {
    brokersRef.value.splice(index, 1);
  }
});

stocksSocket.on('updateStock', (response: StockImprintWithDate) => {
  stockPricesRef.value[response.stockImprint.id] = response.stockImprint.price;
  dateRef.value = response.date;
});

onMounted(() => {
  stocksSocket.emit('findAll');
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