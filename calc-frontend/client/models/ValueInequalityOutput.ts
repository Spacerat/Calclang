/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { ValueOutput } from './ValueOutput';

export type ValueInequalityOutput = {
    lhs: ValueOutput;
    rhs: ValueOutput;
    op: ('>' | '<');
    result: boolean;
    typename?: ValueInequalityOutput.typename;
};

export namespace ValueInequalityOutput {

    export enum typename {
        INEQUALITY = 'inequality',
    }


}

