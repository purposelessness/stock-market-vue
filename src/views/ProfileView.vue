<script setup lang="ts">

import {onMounted, ref} from "vue";

import {Broker} from "@/types/broker";
import {brokersSocket, stocksSocket} from "@/services/gatewayController";
import {StockImprint, StockImprintWithDate} from "@/types/stockImprint";
import BrokerCard from "@/components/brokers/BrokerCard.vue";
import StocksView from "@/views/StocksView.vue";

const loginRef = ref('');
const showPopup = ref(false);

function login() {
  brokersSocket.emit('findByLogin', loginRef.value, (broker: Broker | null) => {
    if (Object.keys(broker).length === 0) {
      loginRef.value = '';
    } else {
      brokerRef.value = broker;
      console.log('Logged in');
      console.log(broker)
    }
  });
}

const brokerRef = ref(null as Broker);
const dateRef = ref('????-??-??');
const stockPricesRef = ref({});

brokersSocket.on('updated', (broker: Broker) => {
  if (broker.login !== loginRef.value) {
    return;
  }
  brokerRef.value = broker;
});

stocksSocket.on('updateStock', (response: StockImprintWithDate) => {
  stockPricesRef.value[response.stockImprint.id] = response.stockImprint.price;
  dateRef.value = response.date;
});

onMounted(() => {
  setTimeout(() => {
    stocksSocket.emit('findAll');
  }, 50);
});

// Set showPopup false when clicked outside popup
window.addEventListener('click', (event: any) => {
  if (event.target.className === 'popup') {
    showPopup.value = false;
  }
});

</script>

<template>
  <div class="register-form">
    <label for="login">Login: </label>
    <input id="login" type="text" v-model="loginRef"/>
    <button id="loginButton" @click="login">Login</button>
  </div>

  <div v-if="brokerRef">
    <div v-if="showPopup" class="popup">
      <div class="popup-content">
        <stocks-view :enabled-buy="true" :broker-id="brokerRef.id"/>
        <button id="closePopupButton" @click="showPopup = false">Close</button>
      </div>
    </div>
    <broker-card v-if="brokerRef" :stock-prices="stockPricesRef" :broker="brokerRef"/>
    <button id="showStocksButton" @click="showPopup = !showPopup">Show stocks</button>
  </div>

  <p v-else>Register first</p>
</template>

<style>

.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;

  background: rgba(0, 0, 0, 0.5);
}

.popup-content {
  position: absolute;
  background: var(--color-background);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: 90%;
}

</style>
