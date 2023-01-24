/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DistributionOutput } from './DistributionOutput';
import type { InequalityProbabilityOutput } from './InequalityProbabilityOutput';
import type { MeasureOutput } from './MeasureOutput';
import type { ValueInequalityOutput } from './ValueInequalityOutput';
import type { ValueOutput } from './ValueOutput';

export type Analysis = {
    name: string;
    outputs: Array<(ValueOutput | MeasureOutput | DistributionOutput | ValueInequalityOutput | InequalityProbabilityOutput)>;
};

