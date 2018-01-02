
function get_volume(dimensions)
    reduce(*, dimensions)
end

input_path = joinpath(dirname(Base.source_path()), "input.txt")
f = open(input_path)
lines = readlines(f)
close(f)

paper = 0
ribbon = 0
for line in lines
    dimensions = split(line, "x")
    dimensions = map(x->parse(Int32, x), dimensions)
    sort!(dimensions)  # sort in-place
    x, y, z = dimensions
    a = 2 * x * y
    b = 2 * x * z
    c = 2 * y * z
    surface = a + b + c
    smallest = Int32(minimum([a, b, c]) / 2)
    paper += surface + smallest

    volume = get_volume(dimensions)
    perimeter = 2 * (x + y)
    ribbon += volume + perimeter
end
println("Paper: ", paper)
println("Ribbon: ", ribbon)
