def strip_schema($drop_title):
  if type != "object" then .
  else
    (if $drop_title then del(.title) else . end)
    | if has("$ref") then .
      else
        with_entries(
          if (.key == "oneOf" or .key == "anyOf" or .key == "allOf")
            and (.value | type == "array") then
            .value |= map(
              if type == "object" and (has("$ref") | not)
              then strip_schema(true)
              else .
              end
            )
          elif .key == "properties" and (.value | type == "object") then
            .value |= with_entries(.value |= strip_schema(false))
          elif .key == "items" and (.value | type == "object") then
            .value |= strip_schema(false)
          elif .key == "prefixItems" and (.value | type == "array") then
            .value |= map(strip_schema(false))
          else .
          end
        )
      end
  end;

if (.components.schemas | type) == "object" then
  .components.schemas |= with_entries(.value |= strip_schema(true))
else .
end
