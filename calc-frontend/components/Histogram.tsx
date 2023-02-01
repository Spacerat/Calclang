import React from "react";

import { Scatter } from "react-chartjs-2";
import { ChartData } from "chart.js";
import { DistributionOutput } from "@/client";
import { zip2, sliding, mid } from "./helpers";

import { Chart, registerables } from "chart.js";

import styles from "./Histogram.module.css";

Chart.register(...registerables);

function Histogram({ distribution }: { distribution: DistributionOutput }) {
  const datasets: ChartData<"scatter"> = {
    datasets: distribution.dists.map((x) => {
      const data = zip2(sliding(x.bins, 2), x.hist).map(
        ([[binLow, binHigh], value]) => ({
          x: mid(binLow, binHigh),
          y: value,
        })
      );

      return {
        label: x.label ?? distribution.distribution.name,
        pointRadius: 2,
        borderColor: "#333",
        backgroundColor: x.color ?? "hsla(349, 88%, 77%, 1)",
        data: data,
        fill: true,
        showLine: true,
      };
    }),
  };

  return (
    <div className={styles.hist}>
      <h3>{distribution.title}</h3>
      <div className={styles.histSize}>
        <Scatter
          title={distribution.title}
          options={{
            responsive: true,
          }}
          data={datasets}
        />
      </div>
    </div>
  );
}

export default React.memo(Histogram);
