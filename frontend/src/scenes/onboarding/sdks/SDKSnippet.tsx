import { Link } from 'lib/lemon-ui/Link'

import { SDK } from '~/types'

export const SDKSnippet = ({ sdk, sdkInstructions }: { sdk: SDK; sdkInstructions: () => JSX.Element }): JSX.Element => {
    return (
        <div>
            <div className="mb-8">
                <h3 className="text-xl font-bold mb-2">Integrate PostHog with {sdk.name}</h3>
                <Link className="" to={sdk.docsLink} target="_blank" targetBlankIcon disableDocsPanel>
                    Read the docs
                </Link>
            </div>
            <div className="deprecated-space-y-4">{sdkInstructions()}</div>
        </div>
    )
}
