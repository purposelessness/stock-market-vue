export interface StockImprintWithDate {
  date: string;
  stockImprint: StockImprint;
}

export interface StockImprint {
  id: number;
  name: string;
  price: number;
  quantity: number;
  enabled: boolean;
}