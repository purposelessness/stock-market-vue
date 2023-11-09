export interface DatePrice {
  date: string;
  price: number;
}

export interface Stock {
  id: number;
  name: string;
  prices: DatePrice[];
  quantity: number;
  enabled: boolean;
}