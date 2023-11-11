"use client"

import {useEffect, useState} from "react";
import Link from "next/link";
import styles from "./page.module.css";

type Leaderboard = {
  id: number;
  name: string;
  score: number;
}

export default function Home() {
  const [data, setData] = useState();
  const [leaderboard, setLeaderboard] = useState<Leaderboard[]>([]);

  useEffect(() => {
    fetch('/api/auth/test')
      .then((res) => res.json())
      .then((res) => {
        setData(res?.data || 'Data from a client');
      })

    fetch('/api/auth/leaderboard')
      .then((res) => res.json())
      .then((res) => {
        setLeaderboard(res?.data || []);
      })

  }, [])
  return (
    <main className={styles.main}>
      <h1 className={styles.title}>Shoot Childrens Scares</h1>
      <p className={styles.subtitle}>
        Point-and-click-игрушка, где надо отстреливать страхи детей.
      </p>

      <div className={styles.buttons}>
        <Link
          href="/second"
          className={
            styles.button + " py-2 px-5 rounded-lg bg-indigo-600 text-white"
          }
        >
          Играть
        </Link>
        <Link
          href="/form/signup"
          className={
            styles.button + " py-2 px-5 rounded-lg bg-indigo-600 text-white"
          }
        >
          Регистрация
        </Link>

        <Link
          href="/form"
          className={
            styles.button + " py-2 px-5 rounded-lg bg-indigo-600 text-white"
          }
        >
          Войти в аккаунт
        </Link>

        {data && <div>Data: {data}</div>}

        {leaderboard.map(item => <div>{item.name} - {item.score}</div>)}
      </div>
    </main>
  );
}
