import type { Stock } from '@/types/stock';

const BASE_URL = 'http://localhost:3000';

const STOCKS_URL = `${BASE_URL}/stocks`;
const CONTROLLER_URL = `${BASE_URL}/controller`;

export async function getStocks(): Promise<Stock[]> {
  const response = await fetch(`${STOCKS_URL}/details`);
  const data: any = await response.json();
  return data as Stock[];
}
