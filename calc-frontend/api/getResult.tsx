import { Analysis, DefaultService } from "@/client";

import { OpenAPI } from "@/client";

OpenAPI.BASE = "https://walrus-app-wpbvo.ondigitalocean.app";

export async function getResult(code: string): Promise<Analysis> {
  const result = await DefaultService.readItemComputeGet(code);
  return result.analysis;
}

export type { Analysis } from "@/client";
