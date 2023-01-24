/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Result } from '../models/Result';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Read Item
     * @param code
     * @returns Result Successful Response
     * @throws ApiError
     */
    public static readItemComputeGet(
        code: string,
    ): CancelablePromise<Result> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/compute',
            query: {
                'code': code,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
