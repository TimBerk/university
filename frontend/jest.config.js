module.exports = {
    clearMocks: true,
    coverageDirectory: "coverage",
    transform: {
        "^.+\\.(js|jsx)$": "<rootDir>/node_modules/babel-jest",
        ".+\\.(css|styl|less|sass|scss)$": "<rootDir>/node_modules/jest-transform-css"
    },
    transformIgnorePatterns: ["<rootDir>/node_modules/"],
    setupFilesAfterEnv: ["<rootDir>/test-setup.js"],
    moduleDirectories: ["node_modules", "src"],
    "coverageThreshold": {
        "global": {
            "branches": 80,
            "functions": 80,
            "lines": 80,
            "statements": -10
        }
    }
}