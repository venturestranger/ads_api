An API for ads microservice.

## Routing:
1. API V1
- `/rest/v1/auth` - for authorization 
- `/rest/v1/ads_items` - a view for ads items
- `/rest/v1/ads_categories` - a view for ads categories

## Authorization:
1. `GET` request on `/rest/v1/auth?key=<API key>` returns a java web token that is necessary to have an access to the other API endpoints 
2. Consequently, any resource access should be requested with `Authorization` header set to `Bearer <token>`

## GET requests:
1. Enables a client to find any record by matching columns `/<route>?<first column name>=<value>&<second column name>=<value>...` + optional sorting and filtration via `&limit_=<a number of records to fetch>&order_by_=<a column to order by>&order_way_=<asc|desc>`
2. Enables a client to make up aggregative queries by using key words, such as `&key_=<column name>` and `&func_=<max|min|avg|count|sum|...>`

Returns a list of matched records

## POST requests:
1. Posts a record on API via `/<route>` and a json request body that specifies column values (see what columns should be specified in model schemas) 

## PUT requests:
1. Updates column values of a record fetched from `/<route>?id=<record id>` to those specified in a json request body (json body might not be filled out, only fields wished to change)

## DELETE requests:
1. Deletes a record fetched from `/<route>?id=<record id>`

## Model schemas
1. ads_items
   - `id` [int] a record identificator
   - `id_user` [int] an owner identificator
   - `id_ads_category` [int] a category identificator to which it belongs
   - `title` [text] the title of a record
   - `picture_url` [text] a set of picture ref links for an ad  
   - `content` [text] a description for an ad
   - `date_publication` [timestamp] a timestamp for a publication date\time
   - `item_price` [int] an item price
   - `location` [text] an ad location 
   - `tel_id` [text] a telegram id to reach out
   - `inst_id` [text] an instagram id to reach out
   - `wa_id` [text] a whatsapp phone number to reach out
   - `phone` [text] a phone number
2. ads_categories
   - `id` [int] a record identificator
   - `name` [text] a category name
   - `is_custom` [bool] flag whether the category created by clients themselves
   - `picture_url` [text] ref link to category picture
3. user_mark_ad
   - `id` [int] a record identificator
   - `id_ad` [int] an id of the marked ad
   - `id_user` [int] an id of the user marking
   - `date` [timtestamp] ref link to category picture
  
An example of a json body for `POST`, `PUT`, and `DELETE` requests:
`
{
  "name": "A",
  "is_custom": false,
  "picture_url": "link"
}
`
