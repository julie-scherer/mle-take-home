from flask import jsonify, Response, request
from . import bp
from .Solution import Solution
import json


@bp.route("", methods=['POST'])
@bp.route("/", methods=['POST'])
@bp.route("/solution", methods=['POST'])
def get_solution():
    if not request.is_json:
        return Response(jsonify({'error': 'Please send a body'}), 400)
    

    '''Get the body of the request/payLoad'''
    body = request.json
    

    '''Validate the request'''
    # Check body contains img_dims and corner_points arguments
    for input_ in ['img_dims', 'corner_points']:
        if input_ not in body:
            return Response(jsonify({'error': f"You are missing {input_} input"}), 400)
    
    '''Run the program'''
    try:
        # Convert image dimensions to tuple
        img_dims = tuple(int(num) for num in body['img_dims'].replace('(', '').replace(')', '').replace('...', '').split(', '))
        
        # Convert corner points to list of tuples
        cps = body['corner_points'].strip('[]').replace('(', '').replace(')', '').replace('...', '').split(', ')
        corner_points = [ ( float(cps[i]), float(cps[i+1]) ) for i in range(0,len(cps),2) ]

        # Run the Python program and get the solution
        sol = Solution()
        output = sol.get_coordinates(img_dims, corner_points)

        # Return the output
        return Response(json.dumps({'solution': f"{output}"}, indent=2), 200)

    except Exception as e:
        return Response(jsonify({'error': e}), 400)