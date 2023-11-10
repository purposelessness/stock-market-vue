<script setup lang="ts">

import {Ref, ref, UnwrapRef, watch} from 'vue';

import {
  CategoryScale,
  Chart as ChartJs,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  TimeScale,
  Title,
  Tooltip,
} from 'chart.js';
import {Line} from 'vue-chartjs';
import 'chartjs-adapter-date-fns';

import type {DatePrice, Stock} from '@/types/stock';

ChartJs.register(
    CategoryScale,
    LinearScale,
    LineElement,
    PointElement,
    Title,
    Tooltip,
    Legend,
    TimeScale,
);

const payload = defineProps<{ stock: Stock, date: string }>();

let data = ref({} as any);
const options = ref({} as any);
const plugins = [
  {
    id: 'tooltipVerticalLine',
    afterDraw: (chart: { tooltip?: any; scales?: any; ctx?: any }) => {
      if (chart.tooltip && chart.tooltip._active && chart.tooltip._active.length) {
        // find coordinates of tooltip
        const activePoint = chart.tooltip._active[0];
        const {ctx} = chart;
        const {x} = activePoint.element;
        const topY = chart.scales.y.top;
        const bottomY = chart.scales.y.bottom;

        // draw vertical line
        ctx.save();
        ctx.beginPath();
        ctx.moveTo(x, topY);
        ctx.lineTo(x, bottomY);
        ctx.lineWidth = 1;
        ctx.strokeStyle = '#999999' as const;
        ctx.stroke();
        ctx.restore();
      }
    },
  },
];

updateOptions();
updateData();

watch(() => payload.date, async () => {
  await updateData();
});
watch(() => payload.stock, async () => {
  await updateOptions();
  await updateData();
});

async function updateOptions() {
  options.value = {
    animation: {
      duration: 0,
    },
    responsive: true,
    plugins: {
      legend: {
        position: 'bottom' as const,
      },
      title: {
        display: true,
        text: payload.stock.name,
      },
    },
    scales: {
      y: {
        beginAtZero: true,
      },
      x: {
        type: 'time' as const,
        time: {
          unit: 'day' as const,
        },
      },
    },
  }
}

async function updateData() {
  const maxDateTime = new Date(payload.date).getTime();
  const minDateTime = new Date(maxDateTime - 1000 * 60 * 60 * 24 * 365).getTime();

  const filteredPairs = payload.stock.prices
      .filter((pair: DatePrice) => {
            const dateTime = new Date(pair.date).getTime();
            return minDateTime <= dateTime && dateTime <= maxDateTime;
          }
      );

  const dates: string[] = [];
  const prices: number[] = [];

  filteredPairs.forEach((pair: DatePrice) => {
    dates.push(pair.date);
    prices.push(pair.price);
  });

  data.value = {
    labels: dates,
    datasets: [
      {
        label: payload.stock.name,
        data: prices,
        fill: false,
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgba(255, 99, 132, 0.5)',
      },
    ],
  };
}

</script>

<template>

  <Line :data="data" :options="options" :plugins="plugins"/>

</template>

<style scoped>

</style>