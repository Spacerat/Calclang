/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DistributionElement } from './DistributionElement';
import type { VarOutput } from './VarOutput';

export type DistributionOutput = {
    title: string;
    distribution: VarOutput;
    dists: Array<DistributionElement>;
    typename?: DistributionOutput.typename;
};

export namespace DistributionOutput {

    export enum typename {
        DISTRIBUTION = 'distribution',
    }


}

