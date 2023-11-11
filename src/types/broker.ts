import type {Active} from "@/types/active";

export interface Broker {
  id: number;
  login: string;
  money: number;
  actives: { id: number, value: Active[] }[]
}