/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type MeasureOutput = {
    kind: MeasureOutput.kind;
    value: number;
    unit: string;
    name: string;
    typename?: MeasureOutput.typename;
};

export namespace MeasureOutput {

    export enum kind {
        MEDIAN = 'median',
        MEAN = 'mean',
    }

    export enum typename {
        MEASURE = 'measure',
    }


}

