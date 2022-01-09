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

#### 3. Clients will be able to get all colour string to RGB mapping

#### 4. Clients will be able to get individual colour string to RGB mapping

#### 5. Authorized users will be allowed to add new colour string to RGB mapping

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

#### 6. Authorized users will be allowed to delete existing colour string to RGB mapping

### Non-functional requirements

1. Must be able to support 1000 concurrent requests
2. Response time must be < 1s
3. Each client is limited to 30 API requests per minute, including routes that requires authentication

## API Endpoint Usage

| No. | Method | URI                           | Request Body                             | Requires Auth |
| --- | ------ | ----------------------------- | ---------------------------------------- | :-----------: |
| 1   | PUT    | `/colours`                    | `{colour: 'orange', rgb: '(255,165,0)'}` |      ✅       |
| 2   | GET    | `/colours`                    | -                                        |      ❌       |
| 3   | GET    | `/colours/{colour-in-string}` | -                                        |      ❌       |
| 4   | DELETE | `/colours/{colour-in-string}` | -                                        |      ✅       |

#### 1. Add/Update colour to RGB decimal

Example:

```http
>> PUT /colours Bearer: true {colour: 'orange', rgb: '(255,165,0)'}

<< {colour: 'orange', rgb: '(255,165,0)'}
```

#### 2. Get all colour to RGB decimal

Example:

```http
>> GET /colours

<< [ {colour: 'red', rgb: '(255,0,0)'}, {colour: 'green', rgb: '(0,255,0)'}, ... ]
```

#### 3. Get RGB decimal from colour

Example:

```http
>> GET /colours/blue

<< {colour: 'blue', rgb: '(0,0,255)'}
```

#### 4. Delete colour to RGB decimal mapping

Example:

```http
>> DELETE /colours/blue

<< {"message": "Successfully deleted blue"}
```
