> For Sourced Group Interview Technical Challenge

# colour-to-rgb-decimal

REST API that when given colour in string format, return RGB decimal value.

'red' → (255,0,0)

'green' → (0,255,0)

'blue' → (0,0,255)

## Assumed Requirements

### Functional Requirements

#### 1. API will support the following colour as version 1

| Colour            | Decimal Code  |
| ----------------- | ------------- |
| black             | (0,0,0)       |
| white             | (255,255,255) |
| red               | (255,0,0)     |
| lime              | (0,255,0)     |
| blue              | (0,0,255)     |
| yellow            | (255,255,0)   |
| cyan / aqua       | (0,255,255)   |
| magenta / fuchsia | (255,0,255)   |
| silver            | (192,192,192) |
| gray              | (128,128,128) |
| maroon            | (128,0,0)     |
| olive             | (128,128,0)   |
| green             | (0,128,0)     |
| purple            | (128,0,128)   |
| teal              | (0,128,128)   |
| navy              | (0,0,128)     |

#### 2. Colour string will always be in lowercase

- When there is a need for a space in colour string, it will be denoted by `-`. For example: `dark-red`

#### 3. Authorized users will be allowed to add new colour string to RGB mapping

- if colour string does not exists, do an upsert
- if colour string exists but the decimal colour are different, do an upsert
- if colour string exists and decimal colour are the same do nothing
- added colour will always will be in the following format, no input verification is required

```json
{
  "colour": "{colour_name_in_string}",
  "rgb": "{rgbDecimalCode}"
}

// e.g
{
  "colour": "green",
  "rgb": "(0,255,0)"
}
```

### Non-functional requirements

1. Must be able to support 1000 concurrent requests
2. Response time must be < 500ms
3. Each client is limited to 30 API requests per minute, including routes that requires authentication

## API Endpoint Usage

| No. | Method | URI                           | Request Body                             | Requires Auth |
| --- | ------ | ----------------------------- | ---------------------------------------- | :-----------: |
| 1   | GET    | `/colours/{colour-in-string}` | -                                        |      ❌       |
| 2   | PUT    | `/colours`                    | `{colour: 'orange', rgb: '(255,165,0)'}` |      ✅       |

#### 1. Get RGB decimal from colour

Example:

```http
>> GET /colours/red

<< {colour: 'red', rgb: '(255,0,0)'}
```

#### 2. Add new colour to RGB mapping

Example:

```http
>> PUT /colours {colour: 'orange', rgb: '(255,165,0)'}

<< {colour: 'orange', rgb: '(255,165,0)'}
```
