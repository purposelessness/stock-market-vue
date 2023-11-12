<script setup lang="ts">

import type {StockImprint} from "@/types/stockImprint";

const payload = defineProps<{ stockImprint: StockImprint }>();

</script>

<template>

  <div class="stock-summary">
    <p>Price: <span id="stockPrice">{{ payload.stockImprint.price ?? 'None' }}</span></p>
    <p>Quantity: {{ payload.stockImprint.quantity ?? 'None' }}</p>
  </div>

</template>

<style scoped>

</style>