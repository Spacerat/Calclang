/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type ValueOutput = {
    value: number;
    unit: string;
    name?: string;
    typename?: ValueOutput.typename;
};

export namespace ValueOutput {

    export enum typename {
        VALUE = 'value',
    }


}

