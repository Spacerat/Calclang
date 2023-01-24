/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { ValueOutput } from './ValueOutput';
import type { VarOutput } from './VarOutput';

export type InequalityProbabilityOutput = {
    distribution: VarOutput;
    threshold: ValueOutput;
    op: ('>' | '<');
    probability: number;
    typename?: InequalityProbabilityOutput.typename;
};

export namespace InequalityProbabilityOutput {

    export enum typename {
        INEQUALITY_PROBABILITY = 'inequality_probability',
    }


}

