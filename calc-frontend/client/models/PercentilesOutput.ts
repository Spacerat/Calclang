/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Percentile } from './Percentile';
import type { VarOutput } from './VarOutput';

export type PercentilesOutput = {
    distribution: VarOutput;
    unit: string;
    percentiles: Array<Percentile>;
    typename?: PercentilesOutput.typename;
};

export namespace PercentilesOutput {

    export enum typename {
        PERCENTILES = 'percentiles',
    }


}

